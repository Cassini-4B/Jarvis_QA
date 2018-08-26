# This script will cluster documents using KMeans clustering based on document vectors


from sklearn.cluster import KMeans, MiniBatchKMeans




def get_clusters(doc_vectors, n_clusters, random_st):
    km = KMeans(n_clusters, random_state=random_st)
    cluster_labels=km.fit_predict(doc_vectors)

    return cluster_labels