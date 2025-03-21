import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    texts = [
        "Stir fry beef - cut the beef into slices, marinate it in baking soda and soy sauce, fry it with oyster sauce, add in chopped vegetables, add in sliced peppers, ",
        "Banana pudding - add vanilla mix into cold water with condensed milk, mix it and let it sit for an hour, whisk whipping cream until stiff peaks, fold the vanilla mix with the whipped cream, add in vanilla wafers and slices of bananas in layers",
        "Roller skates are fun but can take some time to master the skill, however, it is still a great activity to do with kids",
        "EV cars are becoming more popular as we strive to implement optimal energy usage.",
        "When a dragon breathes fire, it usually means it is angry.",
        "Spaghetti and meatballs - buy the spaghetti noodles, cook it, then cook the ground meat with tomato sauce, serve warm.",
        "Labubu is so popular right now everyone is collecting them."
    ]
    
    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]
    
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    print("What do you want to ask today?")
    query_text = input()
    query_vector = model.encode([query_text])[0]
    
    k = 2
    distances, indices = index.search(np.array([query_vector]), k)
    
    print("\n Your closest vector match:")
    for i in range(len(indices[0])):
        print(f"Text: {texts[indices[0][i]]}")
        # print(f"Distance: {distances[0][i]}")
        print()

except Exception as e:
    print(f"an error occured {e}")