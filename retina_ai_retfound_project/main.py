from retina_ai_inference import load_model, analyze_oct

if __name__ == "__main__":
    model = load_model("RETFound_oct_weights.pth")
    result = analyze_oct("example_oct_image.jpg", model)
    print("Диагноз:", result)