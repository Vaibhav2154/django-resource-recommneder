import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(text):
    return model.encode([text])[0]

def recommend_resources(user_interests, resources):
    # Generate user interest embedding
    user_embedding = generate_embeddings(", ".join(user_interests))

    # Calculate similarity scores
    recommendations = []
    for resource in resources:
        resource_embedding = generate_embeddings(resource.title + " " + resource.content)
        similarity = cosine_similarity([user_embedding], [resource_embedding])[0][0]
        recommendations.append((resource, similarity))

    # Sort by similarity score
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return recommendations
