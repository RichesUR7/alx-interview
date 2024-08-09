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
 * Recursively requests and logs the names of characters from an array of URLs.
 *
 * @param {string[]} arr - The array of character URLs.
 * @param {number} i - The current index in the array.
 */
const req = (arr, i) => {
  if (i === arr.length) return; // Base case: end of array
  request(arr[i], (err, response, body) => {
    if (err) {
      console.error('Error fetching character:', err);
    } else {
      console.log(JSON.parse(body).name);
      req(arr, i + 1); // Recursive call for the next character
    }
  });
};

// Fetch the film data
request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      console.error('Error fetching film:', err);
    } else {
      const chars = JSON.parse(body).characters; // Array of character URLs
      req(chars, 0); // Start recursive character fetching
    }
  }
);
