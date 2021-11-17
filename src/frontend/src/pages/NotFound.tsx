import styled from 'styled-components';
import { COLOR_DARK_GREY } from '../utils/cssConstants';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
`;

const NotFound = () => {
  return (
    <Container>
      <span>Not found</span>
    </Container>
  );
};

export default NotFound;
