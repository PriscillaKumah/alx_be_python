# Prompt the user for the current weather

weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendation based on weather condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your unbrella and a raincoat.")
elif weather == "cold": print("Make sure to wear a warm coat and a scarf.")
else: print("Sorry, I don't have recommendations for this weather.")
