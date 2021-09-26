import { SignUpInputs, SignInInputs } from '../interfaces';
import { UserRegisterBody, UserLoginBody } from './interfaces';

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
