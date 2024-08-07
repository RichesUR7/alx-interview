#!/usr/bin/node

/**
 * This script fetches and prints the names of all characters
 * from a specified Star Wars film.
 *
 * Usage: ./0-starwars_characters.js <film_id>
 * Example: ./0-starwars_characters.js 3
 *
 * film_id: The ID of the Star Wars film to fetch characters from.
 *          Valid IDs range from 1 to 6 (corresponding to Episodes I to VI).
 */

const request = require('request');

/**
 * Wraps the 'request' function in a Promise.
 * Sends a GET request to the specified URL and resolves with the name of the character.
 *
 * @param {string} url - The URL of the character resource.
 * @returns {Promise} A Promise that resolves with the name of the character.
 */
const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

/**
 * Fetches the film data from the SWAPI and starts the process of fetching the character data.
 * Sends a GET request to the URL of the film resource and then sends GET requests to the URLs of each character resource.
 * The character names are printed as the responses are received.
 *
 * @param {string} film_id - The ID of the film to fetch data from.
 */
request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      console.error('Error fetching film:', err);
    } else {
      const chars = JSON.parse(body).characters; // Array of character URLs

      // Array of Promises
      const promises = chars.map((url) => requestPromise(url));

      // Wait for all Promises to resolve
      Promise.all(promises)
        .then((names) => {
          // Print all character names
          names.forEach((name) => console.log(name));
        })
        .catch((err) => {
          console.error('Error fetching character:', err);
        });
    }
  }
);
