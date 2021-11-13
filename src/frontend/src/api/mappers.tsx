import { SignUpInputs, SignInInputs, Transaction } from '../interfaces';
import { UserRegisterBody, UserLoginBody, AddTransactionBody } from './interfaces';

export const mapUserRegister = (source: SignUpInputs): UserRegisterBody => {
  return {
    email: source.email,
    password: source.password,
    username: source.username,
  };
};

export const mapUserLogin = (source: SignInInputs): UserLoginBody => {
  return source as UserLoginBody;
};

export const mapAddTransaction = (source: Transaction): AddTransactionBody => {
  return {
    date: source.date.toLocaleDateString(),
    amount: source.amount,
    fee: source.fee,
    price_per_unit: source.price_per_unit,
    record_type: source.record_type,
    symbol: source.symbol,
  }
}