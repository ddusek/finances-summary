import styled from 'styled-components';
import TransactionsHistory from '../components/TransactionsHistory';
import { COLOR_DARK_GREY } from '../utils/cssConstants';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
`

const TransactionsHistoryPage = () => {
  return (
    <Container>
      <TransactionsHistory />
    </Container>
  )
}

export default TransactionsHistoryPage;