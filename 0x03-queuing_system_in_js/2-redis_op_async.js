// Redis Ops Async

// Redis Client

import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

