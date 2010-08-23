#include <posterLib.h>
#include <vimanConst.h>
#include <vimanStruct.h>

typedef enum matrixRef {CameraRef, RobotRef, WorldRef} matrixRef;

/*
 * Expect the name of the poster
 */
POSTER_ID init_data (char*	poster_name, int* ok);

/*
 * Expect a Structure of type VimanObjectPublicArray
 */
int post_viman_poster(POSTER_ID id, VimanObjectPublicArray viman_data);

int real_post_viman_poster(POSTER_ID id, VimanObjectPublicArray* viman_data);

VimanObjectPublicArray generate_viman_struct();

void set_name(VimanObjectPublicArray* viman_data, int index, char* name);
void set_visible(VimanObjectPublicArray* viman_data, int index, int visible);

int write_matrix (VimanObjectPublicArray* viman_data, int index, //matrixRef type,
	double nx, double ny, double nz,
	double ox, double oy, double oz,
	double ax, double ay, double az,
	double px, double py, double pz);

int finalize ( POSTER_ID id );