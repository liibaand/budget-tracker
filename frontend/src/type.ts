export interface User {
    id: number;
    username: string;
  }
  
  export interface BudgetEntry {
    id: number;
    category: string;
    amount: number;
    date: string;
    user_id: number;
  }
  
  export interface AuthResponse {
    message: string;
    user_id?: number;
    error?: string;
  }