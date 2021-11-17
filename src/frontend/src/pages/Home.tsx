import styled from 'styled-components';
import { COLOR_DARK_GREY } from '../utils/cssConstants';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
`;

const Home = () => {
  return (
    <Container>
      <span>home</span>
    </Container>
  );
};

export default Home;
