import api from './base';
import {
  UserRegisterBody,
  UserRegisterResponse,
  UserLoginBody,
  UserLoginResponse,
  UserVerifyResponse,
  AddTransactionBody,
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

export const UserVerify = async (): Promise<
  AxiosResponse<UserVerifyResponse>
> => {
  const response = api.get<UserVerifyResponse>('/user/verify');
  return response;
};

export const AddTransactionReq = async (
  data: AddTransactionBody
): Promise<AxiosResponse<AddTransactionBody>> => {
  const response = api.post('/transaction/add', data);
  return response;
};
