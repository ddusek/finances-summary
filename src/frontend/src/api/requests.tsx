import api from './base';
import {
  UserRegisterBody,
  UserRegisterResponse,
  UserLoginBody,
  UserLoginResponse,
} from './interfaces';
import { AxiosResponse } from 'axios';

export const UserRegister = async (
  data: UserRegisterBody
): Promise<AxiosResponse<UserRegisterResponse>> => {
  const response = api.post<
    UserRegisterBody,
    AxiosResponse<UserRegisterResponse>
  >('/user/register', data);
  return response;
};

export const UserLogin = async (
  data: UserLoginBody
): Promise<AxiosResponse<UserLoginResponse>> => {
  const response = api.post<UserLoginBody, AxiosResponse<UserLoginResponse>>(
    '/user/login',
    data
  );
  return response;
};
