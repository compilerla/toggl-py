package la.compiler.codegen;

import java.io.File;

import io.swagger.codegen.*;
import io.swagger.codegen.languages.PythonClientCodegen;

public class TogglPythonClientCodegen extends PythonClientCodegen {
    public TogglPythonClientCodegen() {
        super();

        modelPackage = "models";
        apiPackage = "api";

        setLibrary("urllib3");
    }

    @Override
    public void processOpts() {
        super.processOpts();

        modelPackage = "models";
        apiPackage = "api";
        final String packageFolder = packageName.replace('.', File.separatorChar);

        supportingFiles.clear();

        supportingFiles.add(new SupportingFile("README.mustache", "", "README.md"));
        supportingFiles.add(new SupportingFile("pyproject.mustache", "", "pyproject.toml"));

        supportingFiles.add(new SupportingFile("configuration.mustache", packageFolder, "configuration.py"));
        supportingFiles.add(new SupportingFile("__init__package.mustache", packageFolder, "__init__.py"));
        supportingFiles.add(new SupportingFile("api_client.mustache", packageFolder, "api_client.py"));
        supportingFiles.add(new SupportingFile("__init__model.mustache",
                packageFolder + File.separatorChar + modelPackage, "__init__.py"));
        supportingFiles.add(new SupportingFile("model_file.mustache", packageFolder + File.separatorChar + modelPackage,
                "file.py"));
        supportingFiles.add(new SupportingFile("__init__api.mustache", packageFolder + File.separatorChar + apiPackage,
                "__init__.py"));
        supportingFiles.add(new SupportingFile("rest.mustache", packageFolder, "rest.py"));

        modelPackage = packageName + "." + modelPackage;
        apiPackage = packageName + "." + apiPackage;
    }

    @Override
    public String getName() {
        return "TogglPythonClientCodegen";
    }
}
