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
