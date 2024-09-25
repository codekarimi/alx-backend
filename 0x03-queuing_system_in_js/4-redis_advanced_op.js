import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => console.log(`Redis client connected to the server`));
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));


// Hash values to store
client.hset("HolbertonSchools", "Portland", 50, redis.print);
client.hset("HolbertonSchools", "Seattle", 80, redis.print);
client.hset("HolbertonSchools", "New York", 20, redis.print);
client.hset("HolbertonSchools", "Bogota", 20, redis.print);
client.hset("HolbertonSchools", "Cali", 40, redis.print);
client.hset("HolbertonSchools", "Paris", 2, redis.print);

//get the values
client.hgetall('HolbertonSchools', (err, res) => {
    if (err) console.error(err.message);
    else console.log(res);
});
