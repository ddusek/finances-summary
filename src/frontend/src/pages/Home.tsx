import styled from 'styled-components';
import { COLOR_DARK_GREY } from '../utils/cssConstants';
import AddTransactionForm from '../components/forms/AddTransaction';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
`;

const Home = () => {
  return (
    <Container>
      <div>
        <AddTransactionForm />
        <AddTransactionForm />
      </div>
      <span>home</span>
    </Container>
  );
};

export default Home;
