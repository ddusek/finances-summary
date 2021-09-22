import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useForm, SubmitHandler } from 'react-hook-form';
import { ErrorMessage } from '@hookform/error-message';
import {
  Form,
  FormLabel,
  SubmitButton,
  Header,
  HeaderContainer,
  ButtonsContainer,
  ButtonContainer,
  ButtonText,
} from '../styled/Form';
import {
  REQUIRED,
  USERNAME_INVALID,
  USERNAME_TOO_LONG,
  EMAIL_TOO_LONG,
  EMAIL_WRONG_FORMAT,
  PASSWORDS_DONT_MATCH,
} from '../../utils/errors';

interface Inputs {
  username: string;
  email: string;
  password: string;
  passwordVerify: string;
}

const emailRegex =
  /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const SignUp: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Inputs>({ criteriaMode: 'all' });

  const [formError, setFormError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [passwordVerifyError, setPasswordVerifyError] = useState('');

  const clearErrors = () => {
    setFormError('');
    setPasswordError('');
    setPasswordVerifyError('');
  };

  const onSubmit: SubmitHandler<Inputs> = (data) => {
    if (data.password !== data.passwordVerify) {
      setPasswordError('field-border-error');
      setPasswordVerifyError('field-border-error');
      setFormError(PASSWORDS_DONT_MATCH);
      return;
    }
    clearErrors();
    console.log(data);
  };

  return (
    <div>
      <HeaderContainer>
        <Header>Sign up</Header>
      </HeaderContainer>
      <Form onSubmit={handleSubmit(onSubmit)}>
        <FormLabel htmlFor="username">
          <input
            placeholder="Username"
            id="username"
            autoComplete="off"
            {...register('username', {
              required: REQUIRED,
              pattern: {
                message: USERNAME_INVALID,
                value: /^[a-zA-Z0-9_]+$/,
              },
              maxLength: {
                value: 20,
                message: USERNAME_TOO_LONG,
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
        </FormLabel>
        <FormLabel htmlFor="email">
          <input
            placeholder="Email"
            id="email"
            autoComplete="off"
            {...register('email', {
              required: REQUIRED,
              pattern: {
                value: emailRegex,
                message: EMAIL_WRONG_FORMAT,
              },
              maxLength: {
                value: 320,
                message: EMAIL_TOO_LONG,
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
        </FormLabel>
        <FormLabel htmlFor="password">
          <input
            className={passwordError}
            placeholder="Password"
            id="password"
            type="password"
            {...register('password', { required: REQUIRED })}
          />
          <span className="field-text">Password</span>
          <ErrorMessage
            errors={errors}
            name="password"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </FormLabel>
        <FormLabel htmlFor="password-verify">
          <input
            className={passwordVerifyError}
            id="password-verify"
            placeholder="Password verify"
            type="password"
            {...register('passwordVerify', { required: REQUIRED })}
          />
          <span className="field-text">Repeat password</span>
          <ErrorMessage
            errors={errors}
            name="passwordVerify"
            render={({ message }) => (
              <span className="field-error">{message}</span>
            )}
          />
        </FormLabel>
        <ButtonsContainer>
          <ButtonContainer>
            <ButtonText className="submit-error">{formError}</ButtonText>
            <SubmitButton type="submit" value="Sign up"></SubmitButton>
          </ButtonContainer>
          <ButtonContainer>
            <ButtonText>Already registered?</ButtonText>
            <Link className="button" to="sign-in">
              Sign in here
            </Link>
          </ButtonContainer>
        </ButtonsContainer>
      </Form>
    </div>
  );
};

export default SignUp;
