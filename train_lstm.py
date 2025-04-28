
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv('data.csv')  # 'text' and 'labels' columns required

# Tokenize text
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
padded = pad_sequences(sequences, maxlen=400)
X_train, X_test, y_train, y_test = train_test_split(padded, df['labels'], test_size=0.2, random_state=0)

# Build LSTM model
model = Sequential()
model.add(layers.Embedding(2000, 40))
model.add(layers.LSTM(100, dropout=0.5))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save model
with open("lstm_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save tokenizer
with open("tokenizer.pkl", "wb") as file:
    pickle.dump(tokenizer, file)

print("✅ LSTM model and tokenizer saved successfully.")
