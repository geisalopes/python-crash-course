def make_shirt(shirt_size, shirt_message):
    """Summarize the shirt that's going to be made."""
    print(
        f"\nThe t-shirt size {shirt_size} has the following message: {shirt_message}."
    )


make_shirt("L", "Eat More Vegetables")
make_shirt(shirt_message="Eat More Fruits", shirt_size="M")
