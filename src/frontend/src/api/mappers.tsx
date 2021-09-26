import { SignUpInputs } from '../types';
import { UserRegisterBody } from './interfaces';

export const mapUserRegister = (source: SignUpInputs): UserRegisterBody => {
  return {
    email: source.email,
    password: source.password,
    username: source.username,
  };
};
