CREATE TRIGGER trigger_artist 
BEFORE INSERT ON Artist 
FOR EACH ROW 
WHEN (NEW.BeginDate < 1000) 
EXECUTE PROCEDURE trigger_call();