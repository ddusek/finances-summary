import React from 'react';
import styled from 'styled-components';
import { COLOR_GREY } from '../constants';
import Form from '../components/forms/SignIn';

const Container = styled.div`
  display: flex;
  justify-content: center;
`;

const SignIn: React.FC = () => {
  return (
    <Container>
      <Form />
    </Container>
  );
};

export default SignIn;
