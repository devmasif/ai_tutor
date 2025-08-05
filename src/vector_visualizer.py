import numpy as np
import plotly.graph_objects as go
from sklearn.manifold import TSNE


class VectorVisualizer:
    def __init__(self, collection):
        self.collection = collection
        
    def visualize_2d(self):
        result = self.collection.get(include=['embeddings', 'documents', 'metadatas'])
        vectors = np.array(result['embeddings'])
        documents = result['documents']
        metadatas = result['metadatas']
        doc_types = [metadata.get('doc_type', 'unknown') for metadata in metadatas]
        
        # Dynamic color mapping for any doc_type
        unique_types = list(set(doc_types))
        print(unique_types)
        color_palette = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
        color_map = {doc_type: color_palette[i % len(color_palette)] for i, doc_type in enumerate(unique_types)}
        colors = [color_map[t] for t in doc_types]

        tsne = TSNE(n_components=2, random_state=42)
        reduced_vectors = tsne.fit_transform(vectors)

        def wrap_text(text, width=80):
            return '<br>'.join([text[i:i+width] for i in range(0, len(text), width)])


        
        fig = go.Figure(data=[go.Scatter(
            x=reduced_vectors[:, 0],
            y=reduced_vectors[:, 1],
            mode='markers',
            marker=dict(size=5, color=colors, opacity=0.8),
            text=[f"Type: {t}<br>Text: {wrap_text(d)}" for t, d in zip(doc_types, documents)],
            hoverinfo = 'text',
            hoverlabel = dict(font=dict(size=10))
        )]
        )
        fig.update_layout(
            title='2D Chroma Vector Store Visualization',
            scene=dict(xaxis_title='x',yaxis_title='y'),
            width=800,
            height=600,
            margin=dict(r=20, b=10, l=10, t=40)
        )
        fig.show()
        
    def visualize_3d(self):
        result = self.collection.get(include=['embeddings', 'documents', 'metadatas'])
        vectors = np.array(result['embeddings'])
        documents = result['documents']
        metadatas = result['metadatas']
        doc_types = [metadata.get('doc_type', 'unknown') for metadata in metadatas]
        
        # Dynamic color mapping for any doc_type
        unique_types = list(set(doc_types))
        color_palette = ['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
        color_map = {doc_type: color_palette[i % len(color_palette)] for i, doc_type in enumerate(unique_types)}
        colors = [color_map[t] for t in doc_types]

        tsne = TSNE(n_components=3, random_state=42)
        reduced_vectors = tsne.fit_transform(vectors)
        
        fig = go.Figure(data=[go.Scatter3d(
            x=reduced_vectors[:, 0],
            y=reduced_vectors[:, 1],
            z=reduced_vectors[:, 2],
            mode='markers',
            marker=dict(size=5, color=colors, opacity=0.8),
            text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
            hoverinfo='text'
        )])
        fig.update_layout(
            title='3D Chroma Vector Store Visualization',
            scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
            width=900,
            height=700,
            margin=dict(r=20, b=10, l=10, t=40)
        )
        fig.show()
