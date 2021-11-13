import React from 'react';
import styled from 'styled-components';
import TransactionsHistory from '../components/TransactionsHistory';
import { COLOR_DARK_GREY } from '../utils/cssConstants';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
`

const TransactionsHistoryPage: React.FC = () => {
  return (
    <Container>
      <TransactionsHistory></TransactionsHistory>
    </Container>
  )
}

export default TransactionsHistoryPage;