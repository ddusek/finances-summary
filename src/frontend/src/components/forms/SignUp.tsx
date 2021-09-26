import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useForm, SubmitHandler } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import { UserRegister, IsSuccessStatus } from '../../api/requests';
import { UserRegisterBody, UserRegisterResponse } from '../../api/interfaces';
import { SignUpInputs } from '../../types';
import { mapUserRegister } from '../../api/mappers';
import * as F from '../styled/Form';
import * as E from '../../utils/errors';
import { AxiosError } from 'axios';

interface FormMessage {
  type: 'error' | 'success' | 'empty';
  msg?: string;
}

const emailRegex =
  /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const getConflictErr = (data: UserRegisterResponse) => {
  if (data.email_conflict && data.username_conflict) {
    return E.CONFLICT_USERNAME_AND_EMAIL;
  } else if (data.username_conflict) {
    return E.CONFLICT_USERNAME;
  }
  return E.CONFLICT_EMAIL;
};

const SignUp: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignUpInputs>({ criteriaMode: 'all' });

  const [formMsg, setFormMsg] = useState<FormMessage>();
  const [passwordError, setPasswordError] = useState('');
  const [passwordVerifyError, setPasswordVerifyError] = useState('');

  const clearErrors = () => {
    setFormMsg({ type: 'empty' });
    setPasswordError('');
    setPasswordVerifyError('');
  };

  const onSubmit: SubmitHandler<SignUpInputs> = async (data) => {
    if (data.password !== data.passwordVerify) {
      setPasswordError('field-border-error');
      setPasswordVerifyError('field-border-error');
      setFormMsg({ type: 'error', msg: E.PASSWORDS_DONT_MATCH });
      return;
    }
    clearErrors();
    const dataBody: UserRegisterBody = mapUserRegister(data);
    const response = await UserRegister(dataBody)
      .then((res) => {
        setFormMsg({ type: 'success', msg: E.REGISTERED_SUCCESSFULLY });
      })
      .catch((err: AxiosError) => {
        console.log(err);
        switch (err?.response?.status) {
          case 409:
            setFormMsg({
              type: 'error',
              msg: getConflictErr(err.response.data),
            });
            return;
          default:
            setFormMsg({ type: 'error', msg: E.UNSPECIFIC_REQUEST_ERROR });
            return;
        }
      });
    console.log(response);
  };

  return (
    <div>
      <F.HeaderContainer>
        <F.Header>Sign up</F.Header>
      </F.HeaderContainer>
      <F.Form onSubmit={handleSubmit(onSubmit)}>
        <F.FormLabel htmlFor="username">
          <input
            placeholder="Username"
            id="username"
            autoComplete="off"
            {...register('username', {
              required: E.REQUIRED,
              pattern: {
                message: E.USERNAME_INVALID,
                value: /^[a-zA-Z0-9_]+$/,
              },
              maxLength: {
                value: 20,
                message: E.USERNAME_TOO_LONG,
              },
            })}
          />
          <span className="field-text">Username</span>
          <ErrorMessage
            errors={errors}
            name="username"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="email">
          <input
            placeholder="Email"
            id="email"
            autoComplete="off"
            {...register('email', {
              required: E.REQUIRED,
              pattern: {
                value: emailRegex,
                message: E.EMAIL_WRONG_FORMAT,
              },
              maxLength: {
                value: 320,
                message: E.EMAIL_TOO_LONG,
              },
            })}
          />
          <span className="field-text">Email</span>
          <ErrorMessage
            errors={errors}
            name="email"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </F.FormLabel>
        <F.FormLabel htmlFor="password">
          <input
            className={passwordError}
            placeholder="Password"
            id="password"
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
        <F.FormLabel htmlFor="password-verify">
          <input
            className={passwordVerifyError}
            id="password-verify"
            placeholder="Password verify"
            type="password"
            {...register('passwordVerify', { required: E.REQUIRED })}
          />
          <span className="field-text">Repeat password</span>
          <ErrorMessage
            errors={errors}
            name="passwordVerify"
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
            <F.ButtonText>Already registered?</F.ButtonText>
            <Link className="button" to="sign-in">
              Sign in here
            </Link>
          </F.ButtonContainer>
        </F.Buttons>
      </F.Form>
    </div>
  );
};

export default SignUp;
