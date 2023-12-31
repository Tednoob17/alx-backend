// Can I have a seat?

import { createQueue } from 'kue';
import { createClient } from 'redis';
import { promisify } from 'util';
import express from 'express';


const queue = createQueue();
const client = createClient({ name: 'reserveSeat'});
const app = express();
let reservationEnabled = false;

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

