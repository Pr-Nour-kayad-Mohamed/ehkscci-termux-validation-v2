# EHK-SCCI V3.4 REAL <50ms - Batched Sinkhorn fixed
import numpy as np, networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.linalg import eigsh

def batched_sinkhorn(D_batch, eps=0.12, n_iter=25):
    E = D_batch.shape[0]
    K = np.exp(-D_batch/eps)
    K = np.clip(K, 1e-100, None)
    a = np.full((E,4), 0.25)
    b = np.full((E,4), 0.25)
    u = np.ones((E,4)); v = np.ones((E,4))
    for _ in range(n_iter):
        u = a / (np.einsum('eij,ej->ei', K, v) + 1e-12)
        v = b / (np.einsum('eij,ei->ej', K, u) + 1e-12)
    P = u[:,:,None]*K*v[:,None,:]
    return np.sum(P*D_batch, axis=(1,2))

def compute_metrics(G):
    nodes=list(G.nodes()); idx={x:i for i,x in enumerate(nodes)}; n=len(nodes)
    row=[]; col=[]; data=[]
    for u,v in G.edges():
        i=idx[u]; j=idx[v]; row+=[i,j]; col+=[j,i]; data+=[1,1]
    mat=csr_matrix((data,(row,col)),shape=(n,n))
    dist=shortest_path(mat, method='D', directed=False, unweighted=True)
    edges=list(G.edges())
    E=len(edges)
    D_batch=np.zeros((E,4,4))
    for e,(u,v) in enumerate(edges):
        Nu=[idx[x] for x in G.neighbors(u)]+[idx[u]]
        Nv=[idx[x] for x in G.neighbors(v)]+[idx[v]]
        D_batch[e]=dist[np.ix_(Nu,Nv)]
    W = batched_sinkhorn(D_batch)
    or_mean=float(np.mean(1-W))
    L=nx.laplacian_matrix(G).astype(float)
    vals,_=eigsh(L, k=2, which='SM', tol=1e-3, maxiter=200)
    lambda2=float(sorted(vals)[1])
    return or_mean, lambda2, E
