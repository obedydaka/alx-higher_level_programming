#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: ./101-starwars_characters.js <Movie ID>');
    process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to fetch data from API. Status code: ${response.statusCode}`);
        return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    const fetchCharacterNames = (urls, index = 0) => {
        if (index >= urls.length) {
            return;
        }

        request(urls[index], (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }

            if (response.statusCode !== 200) {
                console.error(`Failed to fetch data from API. Status code: ${response.statusCode}`);
                return;
            }

            const characterData = JSON.parse(body);
            console.log(characterData.name);
            fetchCharacterNames(urls, index + 1);
        });
    };

    fetchCharacterNames(characters);
});
