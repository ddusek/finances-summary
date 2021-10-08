export interface SignUpInputs {
  username: string;
  email: string;
  password: string;
  passwordVerify: string;
}

export interface SignInInputs {
  login: string;
  password: string;
}

export interface AddTransactionInputs {
  date: Date;
  record_type: 'BUY' | 'SELL';
  symbol: string;
  amount: number;
  price_per_unit: number;
}
