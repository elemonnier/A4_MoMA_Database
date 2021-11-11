CREATE FUNCTION trigger_call()
        RETURNS TRIGGER
        LANGUAGE PLPGSQL
        AS
$$
BEGIN
        RAISE NOTICE 'ERROR: BeginDate is too low (<1000) !';
        RETURN NEW;
END;
$$