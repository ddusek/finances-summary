import React from 'react';
import styled from 'styled-components';
import Form from '../components/forms/SignUp';

const Container = styled.div`
  display: flex;
  justify-content: center;
`;

const SignUp = () => {
  return (
    <Container>
      <Form />
    </Container>
  );
};

export default SignUp;
