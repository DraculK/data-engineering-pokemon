import scrapy
import math


class PokeSpider(scrapy.Spider):
    name = 'pokemon'
    start_urls = [
        'https://pokemondb.net/pokedex/stats/gen1'
    ]

    def parse(self, response):
        pokemons = response.css('table#pokedex tbody tr')
        for pokemon in pokemons:
            second_type = pokemon.css('td.cell-icon a::text').extract()
            if len(second_type) > 1:
                second_type = pokemon.css('td.cell-icon a::text').extract()[1]
            else:
                second_type = math.nan
            yield {
                'id': pokemon.css("td.cell-num span::text").get(),
                'name': pokemon.css("td.cell-name a::text").get(),
                '1st_type': pokemon.css("td.cell-icon a::text").get(),
                '2nd_type': second_type,
                'total': pokemon.css("td.cell-total::text").get(),
                'hp': pokemon.css("td.cell-num::text")[1].get(),
                'attack': pokemon.css("td.cell-num::text")[2].get(),
                'defense': pokemon.css("td.cell-num::text")[3].get(),
                'sp.atk': pokemon.css("td.cell-num::text")[4].get(),
                'sp.def': pokemon.css("td.cell-num::text")[5].get(),
                'speed': pokemon.css("td.cell-num::text")[6].get()
            }

        # melhora: deixar a contagem de gerações dinâmicas
        for idx in range(2, 10):
            next_page = f"https://pokemondb.net/pokedex/stats/gen{idx}"
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
