export interface UserRegisterBody {
  username: string;
  email: string;
  password: string;
}

export interface UserRegisterResponse {
  success: boolean;
  username_conflict: boolean;
  email_conflict: boolean;
  token: string;
  _id: string;
  username: string;
}

export interface UserLoginBody {
  login: string;
  password: string;
}

export interface UserLoginResponse {
  success: boolean;
  username_conflict: boolean;
  email_conflict: boolean;
  token: string;
  _id: string;
  username: string;
}

export interface UserVerifyResponse {
  authorized: boolean;
}

export interface AddTransactionBody {
  date: string;
  record_type: 'BUY' | 'SELL';
  symbol: string;
  amount: number;
  fee?: number;
  price_per_unit: number;
}
