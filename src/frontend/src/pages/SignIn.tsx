import React from 'react';
import styled from 'styled-components';
import Form from '../components/forms/SignIn';

const Container = styled.div`
  display: flex;
  justify-content: center;
`;

const SignIn = () => {
  return (
    <Container>
      <Form />
    </Container>
  );
};

export default SignIn;
