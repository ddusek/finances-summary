export interface MenuItem {
  link: string;
  text: string;
  highlight?: boolean;
}

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

export interface Transaction {
  date: Date;
  record_type: 'BUY' | 'SELL';
  symbol: string;
  amount: number;
  fee?: number;
  price_per_unit: number;
  change_number_today: number;
  change_percent_today: number;
  change_number_sale: number;
  change_percent_sale: number;
}
