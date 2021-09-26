import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useForm, SubmitHandler } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import { UserLogin } from '../../api/requests';
import { UserLoginBody } from '../../api/interfaces';
import { SignInInputs } from '../../interfaces';
import { mapUserLogin } from '../../api/mappers';
import * as F from '../styled/Form';
import * as E from './constants';
import { AxiosError } from 'axios';

interface FormMessage {
  type: 'error' | 'success' | 'empty';
  msg?: string;
}

const SignIn: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignInInputs>({ criteriaMode: 'all' });

  const [formMsg, setFormMsg] = useState<FormMessage>();

  const clearErrors = () => {
    setFormMsg({ type: 'empty' });
  };

  const onSubmit: SubmitHandler<SignInInputs> = async (data) => {
    clearErrors();
    const dataBody: UserLoginBody = mapUserLogin(data);
    await UserLogin(dataBody)
      .then(() => {
        setFormMsg({ type: 'success', msg: E.LOGIN_SUCCESSFUL });
      })
      .catch((err: AxiosError) => {
        switch (err?.response?.status) {
          case 401:
            setFormMsg({ type: 'error', msg: E.WRONG_LOGIN_OR_PASSWORD });
            return;
          default:
            setFormMsg({ type: 'error', msg: E.UNSPECIFIC_REQUEST_ERROR });
            return;
        }
      });
  };

  return (
    <div>
      <F.HeaderContainer>
        <F.Header>Sign up</F.Header>
      </F.HeaderContainer>
      <F.Form onSubmit={handleSubmit(onSubmit)}>
        <F.FormLabel htmlFor="username">
          <input
            id="login"
            placeholder="Login"
            {...register('login', {
              required: E.REQUIRED,
              maxLength: {
                value: 320,
                message: E.LOGIN_TOO_LONG,
              },
            })}
          />
          <span className="field-text">Login</span>
          <ErrorMessage
            errors={errors}
            name="login"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="password">
          <input
            id="password"
            placeholder="Password"
            type="password"
            {...register('password', { required: E.REQUIRED })}
          />
          <span className="field-text">Password</span>
          <ErrorMessage
            errors={errors}
            name="password"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.Buttons>
          <F.ButtonContainer>
            <F.ButtonText className={`submit-${formMsg?.type}`}>
              {formMsg?.msg}
            </F.ButtonText>
            <F.SubmitButton type="submit" value="Sign up"></F.SubmitButton>
          </F.ButtonContainer>
          <F.ButtonContainer>
            <F.ButtonText>Dont have account yet?</F.ButtonText>
            <Link className="button" to="sign-up">
              Sign up here
            </Link>
          </F.ButtonContainer>
        </F.Buttons>
      </F.Form>
    </div>
  );
};

export default SignIn;
