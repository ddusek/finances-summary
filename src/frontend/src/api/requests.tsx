import api from './base';
import { UserRegisterBody, UserRegisterResponse } from './interfaces';
import { AxiosResponse } from 'axios';

export const IsSuccessStatus = (statusCode: number): boolean => {
  return statusCode > 199 && statusCode < 300;
};

export const UserRegister = async (
  data: UserRegisterBody
): Promise<AxiosResponse<UserRegisterResponse>> => {
  const response = api.post<
    UserRegisterBody,
    AxiosResponse<UserRegisterResponse>
  >('/user/register', data);
  return response;
};
