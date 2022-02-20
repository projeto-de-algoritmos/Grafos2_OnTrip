import { Box, Flex, Image, Select, Button } from "@chakra-ui/react";
import logo from "../../assets/logo.png"

export default function Drawer({
  handleDestinationChange,
  handleSourceChange,
  handleSubmit,
  airports
}) {
  return (
    <Flex
      direction="column"
      align="center"
      height="100%"
      width="100%"
      justify="space-around"
    >
      <Box marginTop="40px">
        <Image src={logo} />
      </Box>

      <Box flex="1"
        width="100%"
        padding="30px"
      >
        <form onSubmit={handleSubmit}>
          <Flex
            direction="column"
            align="center"
            width="100%"
          >
            <Select
              placeholder="Onde você está?"
              marginBottom="40px"
              width="100%"
              onChange={handleSourceChange}
              required
            >
              {airports.map(airport => (
                <option value={airport}>{airport}</option>
              ))}
            </Select>
            <Select
              placeholder="Para onde quer ir?"
              marginBottom="40px"
              onChange={handleDestinationChange}
              required
            >
              {airports.map((airport, index) => (
                <option key={index} value={airport}>{airport}</option>
              ))}
            </Select>
            <Button
              colorScheme="blue"
              isFullWidth
              type="submit"
            >
              Button
            </Button>
          </Flex>
        </form>
      </Box >
    </Flex >
  );
}