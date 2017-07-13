const Pokemons = require('./src/pokemon.json')

module.exports = () => {
  const randomPokemon = (total) => (Math.random() * total | 0) + 1
  return Pokemons[randomPokemon(Pokemons.length)]
}
