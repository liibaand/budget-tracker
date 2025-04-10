import axios from 'axios';
import { AuthResponse, BudgetEntry } from './types';

const BASE_URL = 'http://localhost:5000';

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const registerUser = async (username: string, password: string): Promise<AuthResponse> => {
  const response = await api.post('/register', { username, password });
  return response.data;
};

export const loginUser = async (username: string, password: string): Promise<AuthResponse> => {
  const response = await api.post('/login', { username, password });
  return response.data;
};

export const addBudgetEntry = async (entry: Omit<BudgetEntry, 'id'>): Promise<{ message: string }> => {
  const response = await api.post('/add', entry);
  return response.data;
};

export const getEntries = async (userId: number): Promise<BudgetEntry[]> => {
  const response = await api.get(`/entries?user_id=${userId}`);
  return response.data;
};