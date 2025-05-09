import streamlit as st
#20240097
# i had to add this because without it, it kept crashing, something abotut it has to be initalized first
#ai was used for the recipes so its more accurate (i was too lazy to search for cool recepies nd stuff)
if 'recipe_data' not in st.session_state:
    st.session_state.recipe_data = {
        'Spaghetti Carbonara': {
            'Cuisine': 'Italian',
            'Ingredients': ['Spaghetti', 'Eggs', 'Parmesan Cheese', 'Pancetta', 'Black Pepper', 'Salt'],
            'Prep Time': 20,
            'Difficulty': 'Medium',
            'Rating': 4.5
        },
        'Chicken Tikka Masala': {
            'Cuisine': 'Indian',
            'Ingredients': ['Chicken', 'Yogurt', 'Tomato Sauce', 'Cream', 'Garam Masala', 'Ginger', 'Garlic'],
            'Prep Time': 45,
            'Difficulty': 'Hard',
            'Rating': 4.8
        },
        'Avocado Toast': {
            'Cuisine': 'American',
            'Ingredients': ['Bread', 'Avocado', 'Lemon Juice', 'Salt', 'Red Pepper Flakes', 'Olive Oil'],
            'Prep Time': 5,
            'Difficulty': 'Easy',
            'Rating': 3.7
        },
        'Beef Bulgogi': {
            'Cuisine': 'Korean',
            'Ingredients': ['Beef', 'Soy Sauce', 'Sugar', 'Pear', 'Garlic', 'Ginger', 'Sesame Oil'],
            'Prep Time': 30,
            'Difficulty': 'Medium',
            'Rating': 4.6
        },
        'Miso Soup': {
            'Cuisine': 'Japanese',
            'Ingredients': ['Dashi Stock', 'Miso Paste', 'Tofu', 'Wakame Seaweed', 'Green Onions'],
            'Prep Time': 15,
            'Difficulty': 'Easy',
            'Rating': 4.2
        },
        'Chicken Enchiladas': {
            'Cuisine': 'Mexican',
            'Ingredients': ['Chicken', 'Tortillas', 'Enchilada Sauce', 'Cheese', 'Onion', 'Sour Cream'],
            'Prep Time': 40,
            'Difficulty': 'Medium',
            'Rating': 4.4
        },
        'Ratatouille': {
            'Cuisine': 'French',
            'Ingredients': ['Eggplant', 'Zucchini', 'Bell Peppers', 'Tomatoes', 'Onion', 'Garlic', 'Herbs de Provence'],
            'Prep Time': 45,
            'Difficulty': 'Medium',
            'Rating': 4.1
        },
        'Pad Thai': {
            'Cuisine': 'Thai',
            'Ingredients': ['Rice Noodles', 'Shrimp', 'Tofu', 'Bean Sprouts', 'Peanuts', 'Tamarind Sauce', 'Egg'],
            'Prep Time': 35,
            'Difficulty': 'Hard',
            'Rating': 4.7
        },
        'Greek Salad': {
            'Cuisine': 'Greek',
            'Ingredients': ['Cucumber', 'Tomatoes', 'Red Onion', 'Feta Cheese', 'Kalamata Olives', 'Olive Oil', 'Oregano'],
            'Prep Time': 15,
            'Difficulty': 'Easy',
            'Rating': 4.3
        },
        'Beef Bourguignon': {
            'Cuisine': 'French',
            'Ingredients': ['Beef', 'Red Wine', 'Bacon', 'Mushrooms', 'Pearl Onions', 'Carrots', 'Garlic'],
            'Prep Time': 180,
            'Difficulty': 'Hard',
            'Rating': 4.9
        },
        'Vegetable Stir Fry': {
            'Cuisine': 'Chinese',
            'Ingredients': ['Broccoli', 'Bell Peppers', 'Carrots', 'Snow Peas', 'Ginger', 'Garlic', 'Soy Sauce'],
            'Prep Time': 20,
            'Difficulty': 'Easy',
            'Rating': 4.0
        },
        'Shakshuka': {
            'Cuisine': 'Middle Eastern',
            'Ingredients': ['Eggs', 'Tomatoes', 'Bell Peppers', 'Onion', 'Paprika', 'Cumin', 'Feta Cheese'],
            'Prep Time': 25,
            'Difficulty': 'Medium',
            'Rating': 4.5
        },
        'Fish Tacos': {
            'Cuisine': 'Mexican',
            'Ingredients': ['White Fish', 'Corn Tortillas', 'Cabbage', 'Lime', 'Avocado', 'Cilantro', 'Crema'],
            'Prep Time': 30,
            'Difficulty': 'Medium',
            'Rating': 4.4
        },
        'Butter Chicken': {
            'Cuisine': 'Indian',
            'Ingredients': ['Chicken', 'Butter', 'Tomato Sauce', 'Heavy Cream', 'Garam Masala', 'Ginger', 'Garlic'],
            'Prep Time': 50,
            'Difficulty': 'Hard',
            'Rating': 4.8
        },
        'Caprese Salad': {
            'Cuisine': 'Italian',
            'Ingredients': ['Tomatoes', 'Fresh Mozzarella', 'Basil', 'Olive Oil', 'Balsamic Glaze', 'Salt'],
            'Prep Time': 10,
            'Difficulty': 'Easy',
            'Rating': 4.6
        },
        'Bibimbap': {
            'Cuisine': 'Korean',
            'Ingredients': ['Rice', 'Beef', 'Spinach', 'Carrots', 'Zucchini', 'Egg', 'Gochujang'],
            'Prep Time': 50,
            'Difficulty': 'Hard',
            'Rating': 4.7
        }
    }
####################################################################################################
# function to display results so i dont have to repeat this everything, however i did use ai for .markdown the documentation was very confusing
def display_recipe(recipe_name, recipe_details):
    st.subheader(recipe_name)
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f"**Cuisine:** {recipe_details['Cuisine']}")
        st.markdown(f"**Prep Time:** {recipe_details['Prep Time']} mins")
    with cols[1]:
        st.markdown(f"**Difficulty:** {recipe_details['Difficulty']}")
        st.markdown(f"**Rating:** {recipe_details['Rating']}⭐")
    
    st.markdown("**Ingredients:**")
    for ingredient in recipe_details['Ingredients']:
        st.markdown(f"- {ingredient}")
    st.divider()
#divider aswell it was a nice touch gpt reccomended
# layout = wide was found at the last day of this code alot and alot of errors
st.set_page_config(page_title="Recipe Finder", layout="wide")
st.title("🍳 Recipe Finder System")
#egg emoji is just cool
##################################################################################################################################
# Sidebar navigation i liked the idea of the dude who presented first alot of elements were "inspired"
#radio so only one can picked at a time, index=0 is just a placeholder in a way
with st.sidebar:
    st.header("Navigation")
    option = st.radio(
        "Choose an option:",
        ("Get Recommendations", "Search Recipes", "Filter Recipes", "Add Recipe"),
        index=0
    )
#######################################################################################################    
#display cuisines
    if option in ["Get Recommendations", "Add Recipe"]:
        st.divider()
        st.markdown("**Available Cuisines:**")
        cuisines = sorted({details['Cuisine'] for details in st.session_state.recipe_data.values()})
        st.markdown(", ".join(cuisines))
#######################################################################################################
# main area just copies what's chosen on the radio
if option == "Get Recommendations":
    st.header("Get Recipe Recommendations")
    cuisine = st.text_input("Enter your preferred cuisine:", 
                          placeholder="e.g. Italian, Indian, American...",
                          key="rec_cuisine")
    #placeholder was a very very cool discovery
    #.lower was also copied from dude who presented first i liked his idea
    if cuisine:
        cuisines_available = {details['Cuisine'].lower() for details in st.session_state.recipe_data.values()}
        if cuisine.lower() not in cuisines_available:
            st.warning(f"Sorry, we don't have recipes for '{cuisine}'. Try one of these: {', '.join(cuisines)}")
        else:
            matches = [name for name, details in st.session_state.recipe_data.items() 
                       if details['Cuisine'].lower() == cuisine.lower()]
            
            if matches:
                st.success(f"Found {len(matches)} recipes for {cuisine}:")
                for recipe in matches:
                    display_recipe(recipe, st.session_state.recipe_data[recipe])
            else:
                st.info("No recipes found for that cuisine. Try another input.")

elif option == "Search Recipes":
    st.header("Search for a Recipe")
    search_term = st.text_input("Enter recipe name (full or partial):",
                              placeholder="Search by recipe name,Spaghetti Carbonara...)",
                              key="search_term")
 #######################################################################################################   
    if search_term:
        found_recipes = [name for name in st.session_state.recipe_data 
                        if search_term.lower() in name.lower()]
        
        if found_recipes:
            st.success(f"Found {len(found_recipes)} matching recipes:")
            for recipe in found_recipes:
                display_recipe(recipe, st.session_state.recipe_data[recipe])
        else:
            st.error("No matching recipes found. Try a different search term.")
#.success and .error was also very cool
elif option == "Filter Recipes":
    st.header("Filter Recipes")
    
    with st.expander("Filter Options", expanded=True):
        cols = st.columns(3)
        with cols[0]:
            difficulty = st.selectbox("Difficulty Level", 
                                     ["Any", "Easy", "Medium", "Hard"],
                                     key="filter_diff")
        with cols[1]:
            max_time = st.slider("Maximum Prep Time (mins)", 
                                0, 180, 60,
                                key="filter_time")
        with cols[2]:
            min_rating = st.slider("Minimum Rating", 
                                 0.0, 5.0, 3.5, 0.1,
                                 key="filter_rating")
#######################################################################################################
    #select box so you dont type it in, cols just looks cool 
    # Apply filters
    filtered_recipes = []
    for name, details in st.session_state.recipe_data.items():
        if (difficulty == "Any" or details['Difficulty'] == difficulty) and \
           details['Prep Time'] <= max_time and \
           details['Rating'] >= min_rating:
            filtered_recipes.append((name, details))
    #im gonna be honest im not sure what \ meant but it fixed the code i think it just allows it be in different lines
    #using len(filteredrecipies) just counts how many values are in the list
    # i honestly tried to learn lambda but it was complicated on python i watched a guide and ai helped me here it didnt do much but a friend 
    #reccomeneded it
#######################################################################################################
    if filtered_recipes:
        st.success(f"Found {len(filtered_recipes)} recipes matching your criteria:")
        for name, details in sorted(filtered_recipes, key=lambda x: x[1]['Rating'], reverse=True):
            display_recipe(name, details)
    else:
        st.info("No recipes match all your filters. Try adjusting your criteria.")
#.info is a popup
#######################################################################################################
elif option == "Add Recipe":
    st.header("Add a New Recipe")
    
    with st.form("add_recipe_form"):
        name = st.text_input("Recipe Name*", help="Required field")
        cuisine = st.text_input("Cuisine*")
        ingredients = st.text_area("Ingredients* (one per line)", 
                                 help="Enter one ingredient per line")
        prep_time = st.number_input("Preparation Time (minutes)*", 
                                  min_value=0, max_value=240)
        difficulty = st.selectbox("Difficulty Level*", 
                                ["Easy", "Medium", "Hard"])
        rating = st.slider("Rating (0 for unrated)⭐", 
                         0.0, 5.0, 0.0, 0.1)
        
        submitted = st.form_submit_button("Add Recipe")
        
        if submitted:
            # validation
            if not all([name, cuisine, ingredients, prep_time is not None]):
                st.error("Please fill in all required fields (marked with *)")
            else:
                # i love .strip.split so useful
                ingredients_list = [i.strip() for i in ingredients.split('\n') if i.strip()]
                
                # add recipe data to dict
                st.session_state.recipe_data[name] = {
                    'Cuisine': cuisine,
                    'Ingredients': ingredients_list,
                    'Prep Time': prep_time,
                    'Difficulty': difficulty,
                    'Rating': rating if rating > 0 else None
                }
                
                st.success(f"Recipe '{name}' added successfully! BALLOON TIME")
                st.balloons()#cool addon i like it
                
                display_recipe(name, st.session_state.recipe_data[name])
                #alot of the looky ui stuff was ai, such as layout and markdown all the code and the cool stuff was handmade (except lambda im sorry)