const Pokemons = require('./src/pokemonRow.json')

module.exports = () => {
  const randomPokemon = (total) => (Math.random() * total | 0) + 1
  return Pokemons[randomPokemon(Pokemons.length)]
}