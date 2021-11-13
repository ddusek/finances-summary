import React from 'react';
import styled from 'styled-components';
import AddTransactionForm from '../components/forms/AddTransaction';

const Container = styled.div`
  display: flex;
  justify-content: center;
`;

const AddTransaction = () => {
  return (
    <Container>
      <AddTransactionForm />
    </Container>
  );
};

export default AddTransaction;
