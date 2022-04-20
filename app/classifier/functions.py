


import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification
def text_binary_classification(text):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    batch = tokenizer(text, padding=True, truncation=True, max_length=512,
                      return_tensors="pt")

    with torch.no_grad():
        output = model(**batch)
        label_ids = torch.argmax(output.logits, dim=1)
        labels = [model.config.id2label[label_id] for label_id in label_ids.tolist()]
    return labels