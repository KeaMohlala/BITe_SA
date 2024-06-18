function searchRecipe(ingredients) {
  console.log(ingredients);
  alert("ingredients submitted");
}

function recipeSearch(event) {
  event.preventDefault();
  let typeIngredients = document.querySelector("#search-input");
  searchRecipe(typeIngredients.value);
}

let form = document.querySelector("#search-form");
form.addEventListener("submit", recipeSearch);
