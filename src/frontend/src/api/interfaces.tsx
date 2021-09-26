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