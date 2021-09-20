import React from 'react';
import styled from 'styled-components';
import { useForm, SubmitHandler } from 'react-hook-form';
import {
  Form,
  FormLabel,
  SubmitButton,
  Button,
  Header,
  HeaderContainer,
  ButtonsContainer,
  ButtonContainer,
  ButtonText,
} from '../styles/Form';

interface Inputs {
  username: string;
  email: string;
  password: string;
  passwordVerify: string;
}

const emailRegex =
  /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

const SignIn: React.FC = () => {
  const { register, handleSubmit } = useForm<Inputs>();
  const onSubmit: SubmitHandler<Inputs> = (data) => console.log(data);
  return (
    <div>
      <HeaderContainer>
        <Header>Sign up</Header>
      </HeaderContainer>
      <Form action="Post" onSubmit={handleSubmit(onSubmit)}>
        <FormLabel htmlFor="username">
          <input
            placeholder="Username"
            id="username"
            {...register('username', {
              required: true,
              pattern: /^w+$/,
              maxLength: 20,
            })}
          />
          <span>Username</span>
        </FormLabel>
        <FormLabel htmlFor="email">
          <input
            placeholder="Email"
            id="email"
            {...register('email', {
              required: true,
              pattern: emailRegex,
              maxLength: 320,
            })}
          />
          <span>Email</span>
        </FormLabel>
        <FormLabel htmlFor="password">
          <input
            placeholder="Password"
            id="password"
            type="password"
            {...register('password', { required: true })}
          />
          <span>Password</span>
        </FormLabel>
        <FormLabel htmlFor="password-verify">
          <input
            id="password-verify"
            placeholder="Password verify"
            type="password"
            {...register('passwordVerify', { required: true })}
          />
          <span>Repeat password</span>
        </FormLabel>
        <ButtonsContainer>
          <ButtonContainer>
            <SubmitButton type="submit" value="Sign up"></SubmitButton>
          </ButtonContainer>
          <ButtonContainer>
            <ButtonText>Already registered?</ButtonText>
            <Button>Sign in here</Button>
          </ButtonContainer>
        </ButtonsContainer>
      </Form>
    </div>
  );
};

export default SignIn;