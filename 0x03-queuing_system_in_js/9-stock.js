import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

const getItemById = (id) => listProducts.find((item) => item.itemId === id);

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

listProducts.forEach((item) => {
    client.set(`item.${item.itemId}`, item.initialAvailableQuantity);
});

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
};

const app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(item.itemId);
  return res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(item.itemId);
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.itemId });
  }
  reserveStockById(item.itemId, currentQuantity - 1);
  return res.json({ status: 'Reservation confirmed', itemId: item.itemId });
});

app.listen(1245);